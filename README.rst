Kutt cli
========

::

  > pip install kutt

|

::

  > kutt --help

  Usage: kutt [OPTIONS] COMMAND [ARGS]...

  Submit(options):
      -c, --customurl STRING          Custom ID for custom URL
      -p, --password STRING           Password for the URL
      -r, --reuse                     Return last object of target if exists
  Submit(example):
      > kutt submit -c '[CUSTOM]' -p '[PASSWORD]' -r "[URL]"
  Delete(example):
      > kutt delete [URL/ID]
  List(example):
      > kutt list

  Options:
  --help  Show this message and exit.

  Commands:
  delete  Delete a shorted link (Give me url id or url shorted)
  list    List of last 5 URL objects.
  submit  Submit a new short URL
|
