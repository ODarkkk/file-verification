from cx_Freeze import setup, Executable

   setup(

       name="Verify file",

       version="1.0",

       description="Your application description",

       executables=[Executable("program.py")],

   )