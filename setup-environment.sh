#!/bin/sh
# This script sets up a virtual environment if
# you'd like one.

export VIRTUAL_ENV="$PROJECT_DIR/virtualenv-3.7"

# Enter virtual environment
if [ ! -d $VIRTUAL_ENV ]; then
  ver=$(python3 --version)
  if [[ ! $ver =~ "Python 3\.7\.." ]]; then
    echo "Could not create virtualenv:"
    echo "$ver is being used instead of the required version 3.7" 1>&2
    exit 64
  fi
  echo "Creating virtualenv using $ver"
  python3 -m venv --symlinks $VIRTUAL_ENV
fi

export PATH="$VIRTUAL_ENV/bin:$PATH"
unset PYTHONHOME

python -m ipykernel install --user \
  --name Python-Attitude \
  --display-name "Python (Attitude test)"

