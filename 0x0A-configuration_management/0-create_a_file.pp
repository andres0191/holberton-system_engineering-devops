
file{"/tmp/archivo":
	content => "I love Puppet",
	ensure  => present,
	mode    => 744,
	owner   => www-data,
	group   => www-data;
	}
