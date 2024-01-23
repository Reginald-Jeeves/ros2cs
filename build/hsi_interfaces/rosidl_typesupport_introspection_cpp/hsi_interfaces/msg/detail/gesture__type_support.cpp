// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from hsi_interfaces:msg/Gesture.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "hsi_interfaces/msg/detail/gesture__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace hsi_interfaces
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void Gesture_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) hsi_interfaces::msg::Gesture(_init);
}

void Gesture_fini_function(void * message_memory)
{
  auto typed_message = static_cast<hsi_interfaces::msg::Gesture *>(message_memory);
  typed_message->~Gesture();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember Gesture_message_member_array[3] = {
  {
    "gesture",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_INT64,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(hsi_interfaces::msg::Gesture, gesture),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "probability",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(hsi_interfaces::msg::Gesture, probability),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "distance_hands",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(hsi_interfaces::msg::Gesture, distance_hands),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers Gesture_message_members = {
  "hsi_interfaces::msg",  // message namespace
  "Gesture",  // message name
  3,  // number of fields
  sizeof(hsi_interfaces::msg::Gesture),
  Gesture_message_member_array,  // message members
  Gesture_init_function,  // function to initialize message memory (memory has to be allocated)
  Gesture_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t Gesture_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &Gesture_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace hsi_interfaces


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<hsi_interfaces::msg::Gesture>()
{
  return &::hsi_interfaces::msg::rosidl_typesupport_introspection_cpp::Gesture_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, hsi_interfaces, msg, Gesture)() {
  return &::hsi_interfaces::msg::rosidl_typesupport_introspection_cpp::Gesture_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
