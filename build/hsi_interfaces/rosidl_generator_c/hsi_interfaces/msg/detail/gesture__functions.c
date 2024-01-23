// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from hsi_interfaces:msg/Gesture.idl
// generated code does not contain a copyright notice
#include "hsi_interfaces/msg/detail/gesture__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
hsi_interfaces__msg__Gesture__init(hsi_interfaces__msg__Gesture * msg)
{
  if (!msg) {
    return false;
  }
  // gesture
  // probability
  // distance_hands
  return true;
}

void
hsi_interfaces__msg__Gesture__fini(hsi_interfaces__msg__Gesture * msg)
{
  if (!msg) {
    return;
  }
  // gesture
  // probability
  // distance_hands
}

bool
hsi_interfaces__msg__Gesture__are_equal(const hsi_interfaces__msg__Gesture * lhs, const hsi_interfaces__msg__Gesture * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // gesture
  if (lhs->gesture != rhs->gesture) {
    return false;
  }
  // probability
  if (lhs->probability != rhs->probability) {
    return false;
  }
  // distance_hands
  if (lhs->distance_hands != rhs->distance_hands) {
    return false;
  }
  return true;
}

bool
hsi_interfaces__msg__Gesture__copy(
  const hsi_interfaces__msg__Gesture * input,
  hsi_interfaces__msg__Gesture * output)
{
  if (!input || !output) {
    return false;
  }
  // gesture
  output->gesture = input->gesture;
  // probability
  output->probability = input->probability;
  // distance_hands
  output->distance_hands = input->distance_hands;
  return true;
}

hsi_interfaces__msg__Gesture *
hsi_interfaces__msg__Gesture__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  hsi_interfaces__msg__Gesture * msg = (hsi_interfaces__msg__Gesture *)allocator.allocate(sizeof(hsi_interfaces__msg__Gesture), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(hsi_interfaces__msg__Gesture));
  bool success = hsi_interfaces__msg__Gesture__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
hsi_interfaces__msg__Gesture__destroy(hsi_interfaces__msg__Gesture * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    hsi_interfaces__msg__Gesture__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
hsi_interfaces__msg__Gesture__Sequence__init(hsi_interfaces__msg__Gesture__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  hsi_interfaces__msg__Gesture * data = NULL;

  if (size) {
    data = (hsi_interfaces__msg__Gesture *)allocator.zero_allocate(size, sizeof(hsi_interfaces__msg__Gesture), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = hsi_interfaces__msg__Gesture__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        hsi_interfaces__msg__Gesture__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
hsi_interfaces__msg__Gesture__Sequence__fini(hsi_interfaces__msg__Gesture__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      hsi_interfaces__msg__Gesture__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

hsi_interfaces__msg__Gesture__Sequence *
hsi_interfaces__msg__Gesture__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  hsi_interfaces__msg__Gesture__Sequence * array = (hsi_interfaces__msg__Gesture__Sequence *)allocator.allocate(sizeof(hsi_interfaces__msg__Gesture__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = hsi_interfaces__msg__Gesture__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
hsi_interfaces__msg__Gesture__Sequence__destroy(hsi_interfaces__msg__Gesture__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    hsi_interfaces__msg__Gesture__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
hsi_interfaces__msg__Gesture__Sequence__are_equal(const hsi_interfaces__msg__Gesture__Sequence * lhs, const hsi_interfaces__msg__Gesture__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!hsi_interfaces__msg__Gesture__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
hsi_interfaces__msg__Gesture__Sequence__copy(
  const hsi_interfaces__msg__Gesture__Sequence * input,
  hsi_interfaces__msg__Gesture__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(hsi_interfaces__msg__Gesture);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    hsi_interfaces__msg__Gesture * data =
      (hsi_interfaces__msg__Gesture *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!hsi_interfaces__msg__Gesture__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          hsi_interfaces__msg__Gesture__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!hsi_interfaces__msg__Gesture__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
