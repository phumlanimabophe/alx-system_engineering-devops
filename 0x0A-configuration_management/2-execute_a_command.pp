# This Puppet manifest kills a process named killmenow

exec { 'killmenow':
  command => 'pkill -f "killmenow"',
  onlyif  => 'pgrep -f "killmenow"',
}
