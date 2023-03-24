# install package

package { 'flask':
  ensure   => 'version 2.1.0',
  provider => 'pip3',
}
