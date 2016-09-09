"""
The module ``sirara`` exists to provide a wrapper for factorization functions.

Overview
===============================================================================

This provides a wrapper to generate a standard factorization API. This allows
for usage in other functions expecting a standard API.

"""


def factorizer(data_kw, num_atoms_kw, init_kw=None):
    """
        A wrapper that standardizes various factorization functions.

        Args:
            data_kw(str):         Keyword to use for the data.

            num_atoms_kw(str):    Keyword to use for the number of atoms.

            init_kw(str):         Keyword to use for the initial dictionary
                                  (if possible to set).

        Returns:
            callable:             A decorator to use to wrap a function.
    """

    def factorizer_wrapper(a_callable):
        """
            The wrapper of the callable that creates a new standard function.

            Args:
                a_callable(callable):    The callable to wrap.

            Returns:
                callable:                 A decorator to wrap a function.
        """

        def wrapped(data, num_atoms, init=None, *args, **kwargs):
            """
                The wrapped function.
            """

            if init_kw is None:
                assert init is None, \
                    "This function doesn't take an initial argument."
            else:
                if init is not None:
                    kwargs[init_kw] = init

            kwargs[data_kw] = data
            kwargs[num_atoms_kw] = num_atoms

            return a_callable(*args, **kwargs)

        return wrapped

    return factorizer_wrapper
