# Profile maintenance

The README contains the animated original ASCII portrait, biography, linked technology icons, featured projects and contact links. Its content uses GitHub-compatible Markdown and HTML; the page adopts the reader's GitHub theme.

The GitHub Activity section has been removed at the owner's request. The scheduled refresh workflow has also been removed, so it cannot restore that section. Previous activity assets and refresh scripts are retained as historical source files and are not displayed or scheduled.

Build the portrait animation with `python3 scripts/build_portrait_animation.py` and the technology tiles with `python3 scripts/build_stack_icons.py`. These builders require Pillow. The original portrait is preserved in `assets/ascii-portrait.png`.
