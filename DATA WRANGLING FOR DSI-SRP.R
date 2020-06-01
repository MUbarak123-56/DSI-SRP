## DATA WRANGLING FOR DSI-SRP
fifa17 <- read_csv("C:/Users/ganiy/OneDrive/Documents/DSI-SRP/FIFA 17.csv")
head(fifa17, 10)
fifa18 <- read_csv("C:/Users/ganiy/OneDrive/Documents/DSI-SRP/FIFA 18.csv")
head(fifa18,10)
fifa19 <- read_csv("C:/Users/ganiy/OneDrive/Documents/DSI-SRP/FIFA 19.csv")
head(fifa19, 10)

## install.packages("readxl")
library(readxl)
fpl17 <- read_excel("C:/Users/ganiy/OneDrive/Documents/DSI-SRP/FPL 2016-17.xlsx")
head(fpl17, 10)
fpl18 <- read_excel("C:/Users/ganiy/OneDrive/Documents/DSI-SRP/FPL 2017-18.xlsx")
head(fpl18,10)
fpl19 <- read_excel("C:/Users/ganiy/OneDrive/Documents/DSI-SRP/FPL 2018-19.xlsx")
head(fpl19,10)

library(tidyverse)
fifa17_new <- fifa17 %>%
  select('Full Name', age, overall, potential, player_positions)
print(fifa17_new, n = 10, width = Inf)
fifa18_new <- fifa18 %>%
  select('Full Name', age, overall, potential, player_positions)
fifa19_new <- fifa19 %>%
  select('Full Name', age, overall, potential, player_positions)
season17 <- merge(fpl17, fifa17_new, by = 'Full Name')
season18 <- merge(fpl18, fifa18_new, by = 'Full Name')
season19 <- merge(fpl19, fifa19_new, by = 'Full Name')
season17 <- as_tibble(season17)
ncol(season17)
nrow(season17)
print(as_tibble(season17), n = 10, width = Inf)
levels(season17$player_positions)
levels(fifa17_new$player_positions)
levels(season17['player_positions'])
season17
