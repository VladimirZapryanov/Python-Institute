{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "eeb149f4-ab9d-4b52-a7c5-116dac555f63",
   "metadata": {},
   "outputs": [],
   "source": [
    "import sys"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "e68709ab-3773-4e5a-81da-e2e93ef436f7",
   "metadata": {},
   "outputs": [],
   "source": [
    "import sys\n",
    "import math"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "440afba4-54ee-4350-be5f-0e99abad94d7",
   "metadata": {},
   "outputs": [],
   "source": [
    "import sys, math"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "b5ce350d-fcd6-48c9-8cc8-87b597cd89d3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "__breakpointhook__\t__displayhook__\t__doc__\t__excepthook__\t__interactivehook__\t__loader__\t__name__\t__package__\t__spec__\t__stderr__\t__stdin__\t__stdout__\t__unraisablehook__\t_base_executable\t_baserepl\t_clear_internal_caches\t_clear_type_cache\t_current_exceptions\t_current_frames\t_debugmallocstats\t_enablelegacywindowsfsencoding\t_framework\t_get_cpu_count_config\t_getframe\t_getframemodulename\t_git\t_home\t_is_gil_enabled\t_is_interned\t_setprofileallthreads\t_settraceallthreads\t_stdlib_dir\t_vpath\t_xoptions\tactivate_stack_trampoline\taddaudithook\tapi_version\targv\taudit\tbase_exec_prefix\tbase_prefix\tbreakpointhook\tbuiltin_module_names\tbyteorder\tcall_tracing\tcopyright\tdeactivate_stack_trampoline\tdisplayhook\tdllhandle\tdont_write_bytecode\texc_info\texcepthook\texception\texec_prefix\texecutable\texit\tflags\tfloat_info\tfloat_repr_style\tget_asyncgen_hooks\tget_coroutine_origin_tracking_depth\tget_int_max_str_digits\tgetallocatedblocks\tgetdefaultencoding\tgetfilesystemencodeerrors\tgetfilesystemencoding\tgetprofile\tgetrecursionlimit\tgetrefcount\tgetsizeof\tgetswitchinterval\tgettrace\tgetunicodeinternedsize\tgetwindowsversion\thash_info\thexversion\timplementation\tint_info\tintern\tis_finalizing\tis_stack_trampoline_active\tlast_exc\tlast_traceback\tlast_type\tlast_value\tmaxsize\tmaxunicode\tmeta_path\tmodules\tmonitoring\torig_argv\tpath\tpath_hooks\tpath_importer_cache\tplatform\tplatlibdir\tprefix\tps1\tps2\tps3\tpycache_prefix\tset_asyncgen_hooks\tset_coroutine_origin_tracking_depth\tset_int_max_str_digits\tsetprofile\tsetrecursionlimit\tsetswitchinterval\tsettrace\tstderr\tstdin\tstdlib_module_names\tstdout\tthread_info\tunraisablehook\tversion\tversion_info\twarnoptions\twinver\t"
     ]
    }
   ],
   "source": [
    "import sys\n",
    "\n",
    "for name in dir(sys):\n",
    "    print(name, end='\\t')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "b7727913-5622-474c-8ec9-7a25208a4407",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I wanna exit!\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[31mSystemExit\u001b[39m\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\vzapryanov\\AppData\\Local\\anaconda4\\Lib\\site-packages\\IPython\\core\\interactiveshell.py:3707: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.\n",
      "  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)\n"
     ]
    }
   ],
   "source": [
    "import sys\n",
    "\n",
    "def exit():\n",
    "    print('I wanna exit!')\n",
    "\n",
    "exit()\n",
    "sys.exit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "57e2b5cb-da25-49c4-8cdb-01206aba135d",
   "metadata": {},
   "outputs": [
    {
     "ename": "SystemExit",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[31mSystemExit\u001b[39m\n"
     ]
    }
   ],
   "source": [
    "from sys import exit\n",
    "\n",
    "exit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "87f12cfc-2947-477f-9f92-ea016e187ffe",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I wanna exit!\n"
     ]
    }
   ],
   "source": [
    "from sys import exit\n",
    "\n",
    "def exit():\n",
    "    print('I wanna exit!')\n",
    "\n",
    "exit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "93a60344-02af-4b05-bc30-0fad55270315",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sys import *"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "f51e3152-ef2c-4d17-ad2f-568b8e66da3e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import sys # you need to add sys.\n",
    "from sys import * # it's not recommended"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "52b849f6-ae82-4a31-b7a2-e885a6959f71",
   "metadata": {},
   "outputs": [
    {
     "ename": "SystemExit",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[31mSystemExit\u001b[39m\n"
     ]
    }
   ],
   "source": [
    "import sys as s\n",
    "\n",
    "s.exit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "a82dcd35-7820-4d7a-8bf7-bc976f9ee5e6",
   "metadata": {},
   "outputs": [
    {
     "ename": "SystemExit",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[31mSystemExit\u001b[39m\n"
     ]
    }
   ],
   "source": [
    "from sys import exit as bye_bye\n",
    "\n",
    "bye_bye()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ef198fa6-e39d-429c-9c06-dec9867708e1",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
