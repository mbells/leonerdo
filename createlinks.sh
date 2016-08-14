#!/bin/bash
# Run this to create links to OpenCV code that is used here...

OPENCV_ROOT=../opencv
ln -s ${OPENCV_ROOT}/samples/python/common.py .
ln -s ${OPENCV_ROOT}/samples/python/video.py .

ln -s ../tsp-solver/tsp_solver/ tsp_solver
