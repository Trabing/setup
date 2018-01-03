#!/usr/bin/env python3

import json
import re


def valid_hostname(hostname):
    if 0 < len(hostname) < 251: # Logic: 255-len('-999') # TODO Modularize this hard-coded upper-limit.
        if re.match('^[a-zA-Z0-9]+(-[a-zA-Z0-9]+)*$', hostname):
            return hostname
    else:
        valid_hostname(input('ValueError: Invalid hostname. Try again: ')) # Raise an actual ValueError.

def valid_ran_code(ran_code):
    networks = ['nyc1', 'nyc2', 'nyc3', \
                'sfo1', 'sfo2',         \
                'ams2', 'ams3',         \
                'sgp1',                 \
                'lon1',                 \
                'fra1',                 \
                'tor1',                 \
                'blr1']
    if ran_code.lower() in networks:
        return ran_code
    else:
        valid_ran_code(input('ValueError: Invalid ran_code. Try again: ')) # Raise an actual ValueError.

def valid_ram_size(ram_size):
    memories = ['512mb',                           \
                '1gb', '2gb', '3gb', '4gb', '8gb', \
                '16gb', '32gb', '48gb', '64gb']
    if ram_size.lower() in memories:
        return ram_size
    else:
        valid_ram_size(input('ValueError: Invalid ram_size. Try again: ')) # Raise an actual ValueError.

def valid_os_image(os_image):
    machines = ['centos-6-x32', 'centos-6-x64',             \
                'centos-7-x64',                             \
                'debian-7-x32', 'debian-7-x64',             \
                'debian-8-x32', 'debian-8-x64',             \
                'debian-9-x64',                             \
                'fedora-26-x64', 'fedora-26-x64-atomic',    \
                'fedora-27-x64',                            \
                'freebsd-10-3-x64', 'freebsd-10-3-x64-zfs', \
                'freebsd-10-4-x64', 'freebsd-10-4-x64-zfs', \
                'freebsd-11-0-x64', 'freebsd-11-0-x64-zfs', \
                'freebsd-11-1-x64', 'freebsd-11-1-x64-zfs', \
                'ubuntu-14-04-x32', 'ubuntu-14-04-x64',     \
                'ubuntu-16-04-x32', 'ubuntu-16-04-x64',     \
                'ubuntu-17-04-x32', 'ubuntu-17-04-x64',     \
                'ubuntu-17-10-x64']
    if os_image.lower() in machines:
        return os_image
    else:
        valid_os_image(input('ValueError: Invalid os_image. Try again: ')) # Raise an actual ValueError.

def valid_pat_path(pat_path):
    try:
        return open('{pat_path}'.format(pat_path=pat_path), 'r').read()
    except IOError:
        valid_pat_path(input('IOError: Invalid PAT path. Try again: ')) # TODO Raise an actual IOError.

def valid_vm_count(vm_count):
    if 0 < int(vm_count) < 7: # TODO Modularize this hard-coded upper-limit.
        return vm_count
    else:
        valid_vm_count(input('ValueError: Invalid VM count. Try again: ')) # TODO Raise an actual ValueError.

def create_cluster():
    endpoint = 'https://api.digitalocean.com/v2/droplets'
    hostname = str(valid_hostname(input('Hostname: ')))
    api_data = {}
    pa_token = str(valid_pat_path(input('PAT path: ')))
    vm_count = int(valid_vm_count(input('VM count: ')))
    a_header = 'Authorization: Bearer {pa_token}'.format(pa_token=pa_token)
    c_header = 'Content-Type: application/json'
    if vm_count < 2:
        api_data['name'] = hostname
    else:
        api_data['names'] = ['{hostname} {_}'.format(hostname=hostname, _=_) \
                                .replace(' ', '-')                           \
                                for _ in range(vm_count)]
    api_data['region'] = str(valid_ran_code(input('RAN code: ')))
    api_data['size']   = str(valid_ram_size(input('RAM size: ')))
    api_data['image']  = str(valid_os_image(input('OS image: ')))
    endstate = 'curl -X POST "{endpoint}" \
                -d "{api_data}"           \
                -H "{a_header}"           \
                -H "{c_header}"'.format(endpoint=endpoint,             \
                                        api_data=json.dumps(api_data), \
                                        a_header=a_header.strip(),     \
                                        c_header=c_header)
    return re.sub(' +', ' ', endstate)