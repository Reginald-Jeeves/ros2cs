// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from hsi_interfaces:msg/Gesture.idl
// generated code does not contain a copyright notice

#ifndef HSI_INTERFACES__MSG__DETAIL__GESTURE__STRUCT_HPP_
#define HSI_INTERFACES__MSG__DETAIL__GESTURE__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__hsi_interfaces__msg__Gesture __attribute__((deprecated))
#else
# define DEPRECATED__hsi_interfaces__msg__Gesture __declspec(deprecated)
#endif

namespace hsi_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Gesture_
{
  using Type = Gesture_<ContainerAllocator>;

  explicit Gesture_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->gesture = 0ll;
      this->probability = 0.0;
      this->distance_hands = 0.0;
    }
  }

  explicit Gesture_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->gesture = 0ll;
      this->probability = 0.0;
      this->distance_hands = 0.0;
    }
  }

  // field types and members
  using _gesture_type =
    int64_t;
  _gesture_type gesture;
  using _probability_type =
    double;
  _probability_type probability;
  using _distance_hands_type =
    double;
  _distance_hands_type distance_hands;

  // setters for named parameter idiom
  Type & set__gesture(
    const int64_t & _arg)
  {
    this->gesture = _arg;
    return *this;
  }
  Type & set__probability(
    const double & _arg)
  {
    this->probability = _arg;
    return *this;
  }
  Type & set__distance_hands(
    const double & _arg)
  {
    this->distance_hands = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    hsi_interfaces::msg::Gesture_<ContainerAllocator> *;
  using ConstRawPtr =
    const hsi_interfaces::msg::Gesture_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<hsi_interfaces::msg::Gesture_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<hsi_interfaces::msg::Gesture_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      hsi_interfaces::msg::Gesture_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<hsi_interfaces::msg::Gesture_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      hsi_interfaces::msg::Gesture_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<hsi_interfaces::msg::Gesture_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<hsi_interfaces::msg::Gesture_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<hsi_interfaces::msg::Gesture_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__hsi_interfaces__msg__Gesture
    std::shared_ptr<hsi_interfaces::msg::Gesture_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__hsi_interfaces__msg__Gesture
    std::shared_ptr<hsi_interfaces::msg::Gesture_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Gesture_ & other) const
  {
    if (this->gesture != other.gesture) {
      return false;
    }
    if (this->probability != other.probability) {
      return false;
    }
    if (this->distance_hands != other.distance_hands) {
      return false;
    }
    return true;
  }
  bool operator!=(const Gesture_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Gesture_

// alias to use template instance with default allocator
using Gesture =
  hsi_interfaces::msg::Gesture_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace hsi_interfaces

#endif  // HSI_INTERFACES__MSG__DETAIL__GESTURE__STRUCT_HPP_
