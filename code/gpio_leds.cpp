/*
* GPIO LEDs - Turtlebot Ambulance
*
* A very simple program demonstrating how to use the GPIO pins from C++
*
* Compile using: g++ gpio_leds.cpp -lgpiodcxx -o led_test
* Run using: sudo ./led_test
*
* This code depends on libgpiod-dev (there are alternatives equally as capable).
*
* Author: Jack Naylor, Australian Centre for Field Robotics 2023
* Email: jack.naylor@sydney.edu.au
*/



#include <chrono>
#include <iostream>
#include <thread>

#include <gpiod.h>
#include <gpiod.hpp>

using namespace std::literals::chrono_literals;

const int bLedPin = 27;
const int rLedPin = 22;

int main (void)
{
  std::cout << "ACTIVATE: TURTLEBOT AMBULANCE (PROTOTYPE V0.5)\n";
  std::cout << "Be advised the medical capability of this ambulance is severely limited.\n";

  std::this_thread::sleep_for(2000ms);

  gpiod::chip chip("gpiochip0");
  auto line1 = chip.get_line(bLedPin);
  line1.request({"blue_led",
                 gpiod::line_request::DIRECTION_OUTPUT, 
                 0}, 0);
  auto line2 = chip.get_line(rLedPin);
  line2.request({"red_led",
                 gpiod::line_request::DIRECTION_OUTPUT, 
                 0}, 0);
  while (true) {
    line1.set_value(1);
    line2.set_value(0);
    std::cout << "WEEE" << std::endl;
    std::this_thread::sleep_for(200ms);
    line2.set_value(1);
    line1.set_value(0);
    std::cout << "AWWWW" << std::endl;
    std::this_thread::sleep_for(200ms);
  }

  return 0 ;
}