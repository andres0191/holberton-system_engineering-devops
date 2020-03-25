#!/usr/bin/env bash
# Let’s practice using Puppet to make changes to our configuration file.

file_line { 'do not authenticate password':
    ensure    => 'present',
    path      => '/etc/ssh/ssh_config',
    line      => 'PasswordAutentication no',
    match     => 'PasswordAutentication yes';
  }

file_line { 'file private password':
    path      => '/etc/ssh/ssh_config',
    line      => 'IdentityFile ~/.ssh/holberton';
}

