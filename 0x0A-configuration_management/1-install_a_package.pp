# Install an especific version of flask (2.1.0)
exec {'install flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
}
