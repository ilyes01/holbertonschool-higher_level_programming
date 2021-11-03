#!/bin/bash
#fygukhj
curl -sI "$1" | grep "Allow" | cut -d' ' -f2-
