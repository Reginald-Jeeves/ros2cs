// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from hsi_interfaces:msg/Gesture.idl
// generated code does not contain a copyright notice
#include "hsi_interfaces/msg/detail/gesture__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "hsi_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "hsi_interfaces/msg/detail/gesture__struct.h"
#include "hsi_interfaces/msg/detail/gesture__functions.h"
#include "fastcdr/Cdr.h"

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

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif


// forward declare type support functions


using _Gesture__ros_msg_type = hsi_interfaces__msg__Gesture;

static bool _Gesture__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _Gesture__ros_msg_type * ros_message = static_cast<const _Gesture__ros_msg_type *>(untyped_ros_message);
  // Field name: gesture
  {
    cdr << ros_message->gesture;
  }

  // Field name: probability
  {
    cdr << ros_message->probability;
  }

  // Field name: distance_hands
  {
    cdr << ros_message->distance_hands;
  }

  return true;
}

static bool _Gesture__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _Gesture__ros_msg_type * ros_message = static_cast<_Gesture__ros_msg_type *>(untyped_ros_message);
  // Field name: gesture
  {
    cdr >> ros_message->gesture;
  }

  // Field name: probability
  {
    cdr >> ros_message->probability;
  }

  // Field name: distance_hands
  {
    cdr >> ros_message->distance_hands;
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_hsi_interfaces
size_t get_serialized_size_hsi_interfaces__msg__Gesture(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _Gesture__ros_msg_type * ros_message = static_cast<const _Gesture__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name gesture
  {
    size_t item_size = sizeof(ros_message->gesture);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name probability
  {
    size_t item_size = sizeof(ros_message->probability);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name distance_hands
  {
    size_t item_size = sizeof(ros_message->distance_hands);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _Gesture__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_hsi_interfaces__msg__Gesture(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_hsi_interfaces
size_t max_serialized_size_hsi_interfaces__msg__Gesture(
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

  // member: gesture
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: probability
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: distance_hands
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  return current_alignment - initial_alignment;
}

static size_t _Gesture__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_hsi_interfaces__msg__Gesture(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_Gesture = {
  "hsi_interfaces::msg",
  "Gesture",
  _Gesture__cdr_serialize,
  _Gesture__cdr_deserialize,
  _Gesture__get_serialized_size,
  _Gesture__max_serialized_size
};

static rosidl_message_type_support_t _Gesture__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_Gesture,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, hsi_interfaces, msg, Gesture)() {
  return &_Gesture__type_support;
}

#if defined(__cplusplus)
}
#endif
