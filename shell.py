#!/usr/bin/env python3

import json
import os

from wizard.core.wrappers import digitalocean


def run():
    aws_lightsail = ['awsl', 'aws lightsail']
    digital_ocean = ['do', 'digital ocean']
    iaas_platform = aws_lightsail + digital_ocean
    vendor_choice = input('Vendor: ').lower()
    if vendor_choice in iaas_platform:
        if vendor_choice in aws_lightsail:
            pass # TODO
        elif vendor_choice in digital_ocean:
            print(digitalocean.create_cluster())
            # os.system(digitalocean.create_cluster())
    else:
        pass # TODO


if __name__ == '__main__':
    run()