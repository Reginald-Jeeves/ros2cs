// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from hsi_interfaces:msg/Gesture.idl
// generated code does not contain a copyright notice

#ifndef HSI_INTERFACES__MSG__DETAIL__GESTURE__STRUCT_H_
#define HSI_INTERFACES__MSG__DETAIL__GESTURE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/Gesture in the package hsi_interfaces.
typedef struct hsi_interfaces__msg__Gesture
{
  int64_t gesture;
  double probability;
  double distance_hands;
} hsi_interfaces__msg__Gesture;

// Struct for a sequence of hsi_interfaces__msg__Gesture.
typedef struct hsi_interfaces__msg__Gesture__Sequence
{
  hsi_interfaces__msg__Gesture * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} hsi_interfaces__msg__Gesture__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // HSI_INTERFACES__MSG__DETAIL__GESTURE__STRUCT_H_
