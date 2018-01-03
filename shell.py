#!/usr/bin/env python3

import json
import os
import time

from wizard.core.wrappers import digitalocean


def run():
    aws_lightsail = ['awsl', 'aws lightsail']
    digital_ocean = ['do', 'digital ocean']
    iaas_platform = aws_lightsail + digital_ocean
    vendor_choice = input('Vendor: ').lower()
    if vendor_choice in iaas_platform:
        if vendor_choice in aws_lightsail:
            pass                                                                 # FIXME
        elif vendor_choice in digital_ocean:
            os.system('{unix_command} > build-{timestamp_utc}.json'
                        .format(unix_command=digitalocean.create_cluster(), \
                                timestamp_utc=time.time()))
    else:
        pass                                                                     # FIXME


if __name__ == '__main__':
    run()