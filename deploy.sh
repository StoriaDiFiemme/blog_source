#!/bin/bash

rm -fR deploy/*
make publish
cp output/* deploy

cd deploy
git add .
git ci -m "Updated"
git push
