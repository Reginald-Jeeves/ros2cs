// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from hsi_interfaces:msg/Gesture.idl
// generated code does not contain a copyright notice

#ifndef HSI_INTERFACES__MSG__DETAIL__GESTURE__BUILDER_HPP_
#define HSI_INTERFACES__MSG__DETAIL__GESTURE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "hsi_interfaces/msg/detail/gesture__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace hsi_interfaces
{

namespace msg
{

namespace builder
{

class Init_Gesture_distance_hands
{
public:
  explicit Init_Gesture_distance_hands(::hsi_interfaces::msg::Gesture & msg)
  : msg_(msg)
  {}
  ::hsi_interfaces::msg::Gesture distance_hands(::hsi_interfaces::msg::Gesture::_distance_hands_type arg)
  {
    msg_.distance_hands = std::move(arg);
    return std::move(msg_);
  }

private:
  ::hsi_interfaces::msg::Gesture msg_;
};

class Init_Gesture_probability
{
public:
  explicit Init_Gesture_probability(::hsi_interfaces::msg::Gesture & msg)
  : msg_(msg)
  {}
  Init_Gesture_distance_hands probability(::hsi_interfaces::msg::Gesture::_probability_type arg)
  {
    msg_.probability = std::move(arg);
    return Init_Gesture_distance_hands(msg_);
  }

private:
  ::hsi_interfaces::msg::Gesture msg_;
};

class Init_Gesture_gesture
{
public:
  Init_Gesture_gesture()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Gesture_probability gesture(::hsi_interfaces::msg::Gesture::_gesture_type arg)
  {
    msg_.gesture = std::move(arg);
    return Init_Gesture_probability(msg_);
  }

private:
  ::hsi_interfaces::msg::Gesture msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::hsi_interfaces::msg::Gesture>()
{
  return hsi_interfaces::msg::builder::Init_Gesture_gesture();
}

}  // namespace hsi_interfaces

#endif  // HSI_INTERFACES__MSG__DETAIL__GESTURE__BUILDER_HPP_
