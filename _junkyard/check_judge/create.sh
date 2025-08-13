#!/bin/bash

for dir in */; do
  cd "$dir" || continue
  
  if [ -f "submission.zip" ]; then
    echo "Removing $dir/submission.zip"
    rm "submission.zip"
  fi

  if [ "$(ls -A .)" ]; then
    echo "Creating $dir/submission.zip"
    zip -r "submission.zip" ./*
  fi

  cd - > /dev/null || exit
done
