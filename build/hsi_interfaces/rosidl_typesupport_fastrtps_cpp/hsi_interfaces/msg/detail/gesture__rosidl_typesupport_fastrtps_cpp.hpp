// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__rosidl_typesupport_fastrtps_cpp.hpp.em
// with input from hsi_interfaces:msg/Gesture.idl
// generated code does not contain a copyright notice

#ifndef HSI_INTERFACES__MSG__DETAIL__GESTURE__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
#define HSI_INTERFACES__MSG__DETAIL__GESTURE__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_

#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "hsi_interfaces/msg/rosidl_typesupport_fastrtps_cpp__visibility_control.h"
#include "hsi_interfaces/msg/detail/gesture__struct.hpp"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

#include "fastcdr/Cdr.h"

namespace hsi_interfaces
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_hsi_interfaces
cdr_serialize(
  const hsi_interfaces::msg::Gesture & ros_message,
  eprosima::fastcdr::Cdr & cdr);

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_hsi_interfaces
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  hsi_interfaces::msg::Gesture & ros_message);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_hsi_interfaces
get_serialized_size(
  const hsi_interfaces::msg::Gesture & ros_message,
  size_t current_alignment);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_hsi_interfaces
max_serialized_size_Gesture(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace hsi_interfaces

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_hsi_interfaces
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, hsi_interfaces, msg, Gesture)();

#ifdef __cplusplus
}
#endif

#endif  // HSI_INTERFACES__MSG__DETAIL__GESTURE__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
