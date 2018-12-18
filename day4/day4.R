library(dplyr)
library(stringr)
library(lubridate)
library(zoo)
library(data.table)

raw_data <- read.delim("day4.txt",sep="\n",header=F,stringsAsFactors = F)%>%
  mutate(datetime = sub(".*\\[(.*)\\].*", "\\1", V1, perl=TRUE),
         event = str_extract(V1 , "\\](.*)"),
         guard = str_extract(event, "\\d+"))%>%
  mutate(datetime = ymd_hm(datetime))%>%
  arrange(datetime)%>%
  mutate(guard=na.locf(guard))%>%
  mutate(datetime_shifted = shift(datetime,type="lead"))%>%
  mutate(sleep_time = ifelse(grepl("falls asleep",event),datetime_shifted-datetime,0))

guard_summary <- raw_data %>%
  group_by(guard)%>%
  summarise(total_sleep_time = sum(sleep_time))%>%
  arrange(desc(total_sleep_time))

top_guard <- guard_summary$guard[1]

top_guard_data <- raw_data%>%
  filter(guard==top_guard , event=="] falls asleep")

#lubridate::minute(top_guard_data$datetime[1])

minute_counter <- data.frame(minute=seq(0,59),counts=rep(0,60))

for (current_minute in (seq(0,59))){
  minute_count <- 0
  for (row in( seq(1, nrow(top_guard_data)))){
    if(lubridate::minute(top_guard_data[row,]$datetime) <= current_minute && lubridate::minute(top_guard_data[row,]$datetime_shifted) > current_minute){
      minute_count <- minute_count + 1
    }
  }
  minute_counter$counts[current_minute+1] <- minute_count
}


minute_counter <- minute_counter %>%
  arrange(desc(counts))

as.numeric(top_guard) * minute_counter$counts[1]




  
  