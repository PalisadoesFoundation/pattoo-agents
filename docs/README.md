# Pattoo Agent Documentation

## Introduction

`pattoo` agents can be used to easily poll IoT data.

## Terminology

A comprehensive list of `pattoo` terminologies [ can be found here.](GLOSSARY.md)

## Agents
Here is a description of currently supported `pattoo` agents.

| Agent | Description                    |
|--|--|
|[pattoo-os-spoked](PATTOO-OS.md)| Python3 based daemon that presents `pattoo` data via a web API URL. This data can be regularly polled from a central server|
|[pattoo-os-hub](PATTOO-OS.md)| Python3 based daemon that polls `pattoo-os-spoked` APIs for data. (Under development)|
|[pattoo-os-autonomousd](PATTOO-OS.md)| Python3 based daemon that posts  `pattoo` to a central server.|

## JSON Data Format

A comprehensive description of `pattoo` JSON data [ can be found here.](DATA.md)