
#### libraries #########################################################################################################

library(tidyverse)
library(inspectdf)
library(funModeling)

#### loading data ######################################################################################################

raw_data_places <- read_csv('data/places.csv')
raw_data_popular_times_1 <- read_csv('data/popular_times_1.csv')
raw_data_popular_times_2 <- read_csv('data/popular_times_2.csv')

raw_data_popular_times <- union(raw_data_popular_times_1, raw_data_popular_times_2)

save(raw_data_places, file = 'data/200_raw_data_places.Rdata')
save(raw_data_popular_times, file = 'data/200_raw_data_popular_times.Rdata')

rm(raw_data_popular_times_1, raw_data_popular_times_2)

### indentyfying of NA's

nas_places <- inspect_na(raw_data_places)
nas_places %>% show_plot()
nas_times <- inspect_na(raw_data_popular_times)
nas_times  %>% show_plot()

### indefyfying of intresting categories 

raw_only_healthcare <- raw_data_places %>%
  filter(type %in% c('doctor', 'pharmacy', 'dentist', 'hospital')) %>%
  select(-price_level) %>%
  separate(point,',',into = c('x', 'y')) 

raw_only_healthcare %>% inspect_na()

write.table(raw_only_healthcare, file = 'only_healthcare.csv')

