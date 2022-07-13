
# I'm a code cell, click me, then run me!
256 * 60 * 24 # Children × minutes × hours

library(testthat) 
library(IRkernel.testthat)
run_tests({
    test_that("Nothing to check.", {
        expect_equal(TRUE, TRUE, 
            info = "")
    })
})

greet <- function(first_name, last_name) {
  paste("My name is ", last_name, ", ", 
        first_name, " ", last_name, "!", sep = "")
}

# Replace with your first and last name.
# That is, unless your name is already James Bond.
greet("Ivan", "Ivanov")

run_tests({
    test_that("Nothing to check.", {
        expect_equal(TRUE, TRUE, 
            info = "")
    })
})

# Reading in the global temperature data,data
global_temp <- read.csv("datasets/global_temperature.csv")

# Take a look at the first datapoints
head(global_temp)

run_tests({
    test_that("Nothing to check.", {
        expect_equal(TRUE, TRUE, 
            info = "")
    })
})

# Plotting global temperature in degrees celsius by year.
plot(global_temp$year, global_temp$degrees_celsius, 
     type = "l", col = "forestgreen", 
     xlab = "Year", ylab = "Temperature")

run_tests({
    test_that("Nothing to check.", {
        expect_equal(TRUE, TRUE, 
            info = "")
    })
})

library(forecast)
library(ggplot2)

# Converting global_temp into a time series (ts) object.
global_temp_ts <- ts(global_temp$degrees_celsius, 
                     start = global_temp$year[1])

# Forecasting global temperature 50 years into the future 
# using an exponential smoothing state space model (ets).
temperature_forecast <- forecast( ets(global_temp_ts), h = 50)

# Plotting the forecast
autoplot(temperature_forecast)

run_tests({
    test_that("The forecast is plotted", {
        expect_true(! is.null(last_plot()), 
            info = "The forecast should be plotted using autoplot, like this: autoplot(temperature_forecast)")
    })    
})


# Are you ready to get started with  DataCamp projects?
I_am_ready <- TRUE

# Ps. 
# Feel free to try out any other stuff in this notebook. 
# It's all yours!

run_tests({
    test_that("The student is ready", {
        expect_equal(I_am_ready, TRUE, 
            info ="I_am_ready should be set to TRUE, if you are ready to get started with DataCamp projects, that is.")
    })
})
