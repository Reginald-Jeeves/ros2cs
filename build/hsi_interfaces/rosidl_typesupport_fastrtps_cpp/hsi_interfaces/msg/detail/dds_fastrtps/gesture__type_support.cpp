// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from hsi_interfaces:msg/Gesture.idl
// generated code does not contain a copyright notice
#include "hsi_interfaces/msg/detail/gesture__rosidl_typesupport_fastrtps_cpp.hpp"
#include "hsi_interfaces/msg/detail/gesture__struct.hpp"

#include <limits>
#include <stdexcept>
#include <string>
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_fastrtps_cpp/wstring_conversion.hpp"
#include "fastcdr/Cdr.h"


// forward declaration of message dependencies and their conversion functions

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
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: gesture
  cdr << ros_message.gesture;
  // Member: probability
  cdr << ros_message.probability;
  // Member: distance_hands
  cdr << ros_message.distance_hands;
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_hsi_interfaces
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  hsi_interfaces::msg::Gesture & ros_message)
{
  // Member: gesture
  cdr >> ros_message.gesture;

  // Member: probability
  cdr >> ros_message.probability;

  // Member: distance_hands
  cdr >> ros_message.distance_hands;

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_hsi_interfaces
get_serialized_size(
  const hsi_interfaces::msg::Gesture & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: gesture
  {
    size_t item_size = sizeof(ros_message.gesture);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: probability
  {
    size_t item_size = sizeof(ros_message.probability);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: distance_hands
  {
    size_t item_size = sizeof(ros_message.distance_hands);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_hsi_interfaces
max_serialized_size_Gesture(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;


  // Member: gesture
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: probability
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: distance_hands
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  return current_alignment - initial_alignment;
}

static bool _Gesture__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const hsi_interfaces::msg::Gesture *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _Gesture__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<hsi_interfaces::msg::Gesture *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _Gesture__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const hsi_interfaces::msg::Gesture *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _Gesture__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_Gesture(full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}

static message_type_support_callbacks_t _Gesture__callbacks = {
  "hsi_interfaces::msg",
  "Gesture",
  _Gesture__cdr_serialize,
  _Gesture__cdr_deserialize,
  _Gesture__get_serialized_size,
  _Gesture__max_serialized_size
};

static rosidl_message_type_support_t _Gesture__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_Gesture__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace hsi_interfaces

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_hsi_interfaces
const rosidl_message_type_support_t *
get_message_type_support_handle<hsi_interfaces::msg::Gesture>()
{
  return &hsi_interfaces::msg::typesupport_fastrtps_cpp::_Gesture__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, hsi_interfaces, msg, Gesture)() {
  return &hsi_interfaces::msg::typesupport_fastrtps_cpp::_Gesture__handle;
}

#ifdef __cplusplus
}
#endif
