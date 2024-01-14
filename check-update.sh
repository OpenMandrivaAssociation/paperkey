#!/bin/sh
curl -L "https://www.jabberwocky.com/software/paperkey/" 2>/dev/null |sed -ne 's,.*paperkey-\(.*\).tar.gz\".*,\1,p'

