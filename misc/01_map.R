library(magrittr)
warsaw_wgs84 <- 
  read.table('data/warsaw_05_wgs84.txt') %>%
  set_colnames(c('longitude', 'latitude', 'district_n', 'district_name'))

library(ggplot2)
library(maps)
library(ggmap)
library(ggthemes)

ggplot(warsaw_wgs84, aes(x = longitude, y = latitude, col = district_name)) +
  geom_point() +
  coord_map() + 
  theme_minimal() +
  guides(col = guide_legend(title = 'District')) +
  labs(title = 'Warsaw') 
ggsave('plots/warsaw_05_wgs84.png')
