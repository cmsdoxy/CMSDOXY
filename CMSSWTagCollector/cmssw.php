<?php
$ver = '';
// if ver parameter exists
if(isset($_GET['ver'])) $ver = escapeshellarg($_GET['ver']);

exec("python26 cmssw.py $ver", $output);

foreach($output as $line) echo "$line\n";
?>
