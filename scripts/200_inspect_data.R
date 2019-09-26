
#### libraries #########################################################################################################

library(tidyverse)
library(inspectdf)

#### loading data ######################################################################################################

raw_data_places <- read_csv('data/places.csv')
raw_data_popular_times_1 <- read_csv('data/popular_times_1.csv')
raw_data_popular_times_2 <- read_csv('data/popular_times_2.csv')

raw_data_popular_times <- union(raw_data_popular_times_1, raw_data_popular_times_2)

rm(raw_data_popular_times_1, raw_data_popular_times_2)

### indentyfying of NA's

nas_places <- inspect_na(raw_data_places)
nas_places %>% show_plot()
nas_times <- inspect_na(raw_data_popular_times)
nas_times  %>% show_plot()
