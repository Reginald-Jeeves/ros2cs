// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from hsi_interfaces:msg/Gesture.idl
// generated code does not contain a copyright notice

#ifndef HSI_INTERFACES__MSG__DETAIL__GESTURE__TRAITS_HPP_
#define HSI_INTERFACES__MSG__DETAIL__GESTURE__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "hsi_interfaces/msg/detail/gesture__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace hsi_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const Gesture & msg,
  std::ostream & out)
{
  out << "{";
  // member: gesture
  {
    out << "gesture: ";
    rosidl_generator_traits::value_to_yaml(msg.gesture, out);
    out << ", ";
  }

  // member: probability
  {
    out << "probability: ";
    rosidl_generator_traits::value_to_yaml(msg.probability, out);
    out << ", ";
  }

  // member: distance_hands
  {
    out << "distance_hands: ";
    rosidl_generator_traits::value_to_yaml(msg.distance_hands, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Gesture & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: gesture
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "gesture: ";
    rosidl_generator_traits::value_to_yaml(msg.gesture, out);
    out << "\n";
  }

  // member: probability
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "probability: ";
    rosidl_generator_traits::value_to_yaml(msg.probability, out);
    out << "\n";
  }

  // member: distance_hands
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "distance_hands: ";
    rosidl_generator_traits::value_to_yaml(msg.distance_hands, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Gesture & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace hsi_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use hsi_interfaces::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const hsi_interfaces::msg::Gesture & msg,
  std::ostream & out, size_t indentation = 0)
{
  hsi_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use hsi_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const hsi_interfaces::msg::Gesture & msg)
{
  return hsi_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<hsi_interfaces::msg::Gesture>()
{
  return "hsi_interfaces::msg::Gesture";
}

template<>
inline const char * name<hsi_interfaces::msg::Gesture>()
{
  return "hsi_interfaces/msg/Gesture";
}

template<>
struct has_fixed_size<hsi_interfaces::msg::Gesture>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<hsi_interfaces::msg::Gesture>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<hsi_interfaces::msg::Gesture>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // HSI_INTERFACES__MSG__DETAIL__GESTURE__TRAITS_HPP_
