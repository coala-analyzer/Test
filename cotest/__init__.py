import os
import tempfile
from site import getsitepackages

from cotest.TestExecution import (parse_args,
                                  create_argparser,
                                  run_tests,
                                  get_test_files,
                                  delete_coverage)


def _main():
    parser = create_argparser(description="Runs tests.")

    args = parse_args(parser)
    (test_files,
     test_file_names) = get_test_files(
        os.path.abspath("."),
        test_only=args.test_only,
        omit=args.omit)

    ignore_list = ([os.path.join(x, "**") for x in getsitepackages()] +
                   [os.path.join(tempfile.gettempdir(), "**")])

    return run_tests(ignore_list,
                     args,
                     test_files,
                     test_file_names)


def main():
    try:
        return _main()
    except KeyboardInterrupt:
        print("Program terminated by user.")
        print("Cleaning up...")
        delete_coverage(silent=True)
        print("Done!")
        return 130
