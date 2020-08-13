#!/bin/bash
echo $(squeue | sed '/kaclark/!d')
