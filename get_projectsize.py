#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 06:17:47 2019

@author: kan

Shut up Spyder, you know I love you for code quickies.
"""
import json
import pathlib
import urllib3
import certifi

https = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where(),
)
base_url = 'https://pypi.org/pypi/$name/json'


def _get_size(package_name: str, version: str = None, packagetype: str = 'bdist_wheel'):
    r = https.request('GET', base_url.replace('$name', package_name))
    if packagetype == 'bdist_wheel':
        packagetype_ = 0
    elif packagetype == 'sdist':
        packagetype_ = 1
    else:
        raise NotImplementedError

    # response code handling could be advanced
    if r.status == 200:
        data = json.loads(r.data.decode('utf-8'))
        if version and version in list(data['releases']):
            size = data['releases'][version][packagetype_]['size']
        else:
            size = data['releases']['urls'][packagetype_]['size']
    else:
        size = -1
    return size


def _read_requirements(location: str = 'requirements.txt'):
    with open(pathlib.Path(location), 'r') as f:
        packages = f.readlines()
    package_list = [x.strip() for x in packages]
    return package_list


def _loop(location: str = 'requirements.txt', packagetype: str = 'bdist_wheel'):
    """asyncable - speed me up"""
    package_list = _read_requirements(location)
    results = []
    for name in package_list:
        package_name, version = name.split('==')
        size = _get_size(package_name, version, packagetype)
        results.append({
            'packagename': name,
            'version': version,
            'size': size
        })
    return results


if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument('--requirements', help='location of requirements', default='requirements.txt')
    p.add_argument('--packagetype', help='bdist_wheel', default='bdist_wheel')
    args = p.parse_args()

    results = _loop(args.requirements, args.packagetype)
    _size = [r['size'] for r in results]
    _total_size = sum(_size) / 1000
    for r in results:
        print(r)
    print(f'total: {_total_size:.0f} kb - {_total_size / 1000:.03f} Mb')
