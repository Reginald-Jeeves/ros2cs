// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from hsi_interfaces:msg/Gesture.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "hsi_interfaces/msg/detail/gesture__struct.h"
#include "hsi_interfaces/msg/detail/gesture__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool hsi_interfaces__msg__gesture__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[36];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("hsi_interfaces.msg._gesture.Gesture", full_classname_dest, 35) == 0);
  }
  hsi_interfaces__msg__Gesture * ros_message = _ros_message;
  {  // gesture
    PyObject * field = PyObject_GetAttrString(_pymsg, "gesture");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->gesture = PyLong_AsLongLong(field);
    Py_DECREF(field);
  }
  {  // probability
    PyObject * field = PyObject_GetAttrString(_pymsg, "probability");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->probability = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // distance_hands
    PyObject * field = PyObject_GetAttrString(_pymsg, "distance_hands");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->distance_hands = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * hsi_interfaces__msg__gesture__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of Gesture */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("hsi_interfaces.msg._gesture");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "Gesture");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  hsi_interfaces__msg__Gesture * ros_message = (hsi_interfaces__msg__Gesture *)raw_ros_message;
  {  // gesture
    PyObject * field = NULL;
    field = PyLong_FromLongLong(ros_message->gesture);
    {
      int rc = PyObject_SetAttrString(_pymessage, "gesture", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // probability
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->probability);
    {
      int rc = PyObject_SetAttrString(_pymessage, "probability", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // distance_hands
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->distance_hands);
    {
      int rc = PyObject_SetAttrString(_pymessage, "distance_hands", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
