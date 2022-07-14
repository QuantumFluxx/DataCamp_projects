
# Load in the tidyverse package
library(tidyverse)

# Read datasets/yearly_deaths_by_clinic.csv into yearly
yearly <- read_csv("datasets/yearly_deaths_by_clinic.csv")

# Print out yearly
yearly

library(testthat) 
library(IRkernel.testthat)
run_tests({
    test_that("Read in data correctly.", {
        expect_is(yearly, "tbl_df", 
            info = 'You should use read_csv (with an underscore) to read "datasets/yearly_deaths_by_clinic.csv" into yearly.')
    })
    
    test_that("Read in data correctly.", {
        yearly_temp <- read_csv('datasets/yearly_deaths_by_clinic.csv')
        expect_equivalent(yearly, yearly_temp, 
            info = 'yearly should contain the data in "datasets/yearly_deaths_by_clinic.csv"')
    })
})

# Adding a new column to yearly with proportion of deaths per no. births
yearly <- yearly %>%
    mutate(proportion_deaths=deaths / births)

# Print out yearly
yearly

run_tests({
    test_that("A proportion_deaths column exists", {
        expect_true("proportion_deaths" %in% names(yearly), 
            info = 'yearly should have the new column proportion_deaths')
    })
    
    test_that("Read in data correctly.", {
        yearly_temp <- read_csv('datasets/yearly_deaths_by_clinic.csv') %>% 
          mutate(proportion_deaths = deaths / births)
        expect_equivalent(yearly, yearly_temp, 
            info = 'proportion_deaths should be calculated as deaths / births')
    })
})

# Setting the size of plots in this notebook
options(repr.plot.width=7, repr.plot.height=4)

# Plot yearly proportion of deaths at the two clinics
ggplot(yearly, aes(x = year, y = proportion_deaths, color = clinic)) +
    geom_line()

run_tests({
    test_that("The right columns are plotted", {
        mappings <- str_replace(as.character(last_plot()$mapping), "~", "")
        expect_true(all(c("year", "proportion_deaths", "clinic") %in% mappings),
                    info = "year should be on the x-axis, proportion_deaths should be on the y-axis, and clinic should be mapped to color.")
    })
})


# Read datasets/monthly_deaths.csv into monthly
monthly <- read_csv("datasets/monthly_deaths.csv")

# Adding a new column with proportion of deaths per no. births
monthly <- monthly %>%
    mutate(proportion_deaths= deaths / births)

# Print out the first rows in monthly
head(monthly)

run_tests({
    
   test_that("Read in data correctly.", {
        expect_is(monthly, "tbl_df", 
            info = 'You should use read_csv (with an underscore) to read "datasets/monthly_deaths.csv" into monthly.')
    })
    
    test_that("Read in monthly correctly.", {
        monthly_temp <- read_csv("datasets/monthly_deaths.csv")
        expect_true(all(names(monthly_temp) %in% names(monthly)), 
            info = 'monthly should contain the data in "datasets/monthly_deaths.csv"')
    })
    
    test_that("proportion_death is calculated correctly.", {
        monthly_temp <- read_csv("datasets/monthly_deaths.csv")
        monthly_temp <- monthly_temp %>% 
          mutate(proportion_deaths = deaths / births)
        expect_equivalent(monthly, monthly_temp, 
            info = 'proportion_deaths should be calculated as deaths / births')
    })
})

# Plot monthly proportion of deaths
ggplot(monthly, aes(x = date, y = proportion_deaths)) +
    geom_line() +
    labs(title = "The effect of handwashing", x = "Year", y = "Proportion deaths")

run_tests({
    test_that("The right columns are plotted", {        
        mappings <- str_replace(as.character(last_plot()$mapping), "~", "")
        expect_true(all(c("date", "proportion_deaths") %in% mappings), 
            info = "date should be on the x-axis, proportion_deaths on the y-axis")
    })
})

# From this date handwashing was made mandatory
handwashing_start = as.Date('1847-06-01')

# Add a TRUE/FALSE column to monthly called handwashing_started
monthly <- monthly %>%
    mutate(handwashing_started = date >= handwashing_start)

# Plot monthly proportion of deaths before and after handwashing
ggplot(monthly, aes(x = date, y = proportion_deaths, color = handwashing_started)) +
    geom_line() +
    labs(title = "The effect of handwashing highlighted", x = "Year", y = "Proportion deaths")

run_tests({
    test_that("handwashing_started has been defined", {
        expect_true("handwashing_started" %in% names(monthly),
            info = 'monthly should contain the column handwashing_started.')
    })  
    
    test_that("there are 22 rows where handwashing_started is TRUE", {
        expect_equal(22, sum(monthly$handwashing_started),
            info = 'handwashing_started should be a TRUE/FALSE column where the rows where handwashing was enforced are set to TRUE.')
    })
    
    test_that("The right columns are plotted", {        
        mappings <- str_replace(as.character(last_plot()$mapping), "~", "")
        expect_true(all(c("date", "proportion_deaths", "handwashing_started") %in% mappings), 
            info = 'date should be on the x-axis, proportion_deaths on the y-axis, and handwashing_started should be mapped to color.')
    })
})

# Calculating the mean proportion of deaths 
# before and after handwashing.

monthly_summary <- monthly %>%
    group_by(handwashing_started) %>%
    summarise(mean_proportion_deaths = mean(proportion_deaths))

# Printing out the summary.
monthly_summary

run_tests({
    test_that("mean_proportion_deaths was calculated correctly", {
        flat_summary <- as.numeric(unlist(monthly_summary))
        handwashing_start = as.Date('1847-06-01')
        monthly_temp <- read_csv("datasets/monthly_deaths.csv") %>% 
          mutate(proportion_deaths = deaths / births) %>% 
          mutate(handwashing_started = date >= handwashing_start) %>% 
          group_by(handwashing_started) %>%
          summarise(mean_proportion_deaths = mean(proportion_deaths))
        expect_true(all(monthly_temp$mean_proportion_deaths %in% flat_summary),
            info = 'monthly_summary should contain the mean monthly proportion of deaths before and after handwashing was enforced.')
    })  
})

# Calculating a 95% Confidence intrerval using t.test 
test_result <- t.test( proportion_deaths ~ handwashing_started, data = monthly)
test_result

run_tests({
    test_that("the confidence intervals match", {
        temp_test_result <- t.test( proportion_deaths ~ handwashing_started, data = monthly)
        expect_equivalent(test_result$conf.int, temp_test_result$conf.int,
            info = 'The t-test should be calculated with proportion_deaths as a function of handwashing_started.')
    })  
})

# The data Semmelweis collected points to that:
doctors_should_wash_their_hands <- TRUE

run_tests({
    test_that("The project is finished.", {
        expect_true(doctors_should_wash_their_hands, 
            info = "Semmelweis would argue that doctors_should_wash_their_hands should be TRUE .")
    })  
})
