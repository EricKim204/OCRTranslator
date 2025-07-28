# OCR Translator Extension

A browser extension that translates text from images on any webpage 

## Project Overview

This extension allows users to click on any image within a webpage, automatically extract visible text, translate it into a target language, and overlay the translated text on top of the original image in-place.

## Core Features (Planned)

- Detect and select images on webpages
- Extract embedded text from the image
- Translate the extracted text to a target language
- Overlay the translated text on the image using a transparent or styled layer

## Development Plan
### Stage 1: Python Proof of Concept

Build a simple Python script to test the key features:
- Extract text from an image using OCR
- Translate the text to another language
- Overlay the translation back onto the image

---

### Stage 2: Browser Extension

Build a Chrome extension to apply the same logic on images within webpages:
1. Detect and handle image clicks
2. Run OCR and translation in the browser or via an API
3. Overlay the translated text on the image in-place
4. Add basic UI for language selection and settings


### Stage 3: Advanced Features

Mobile Support (?): React Native app for mobile browsers