import os

import taggernoter
import argparse

taggernoter.app.ApplicationCLI.run(argparse.Namespace(**{
    "configuration": "./debug.configuration.json",
}))

