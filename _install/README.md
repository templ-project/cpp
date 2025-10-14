# Bootstrap Script

This directory contains the bootstrap script for setting up new C++ projects from this template.

## Usage

### Quick Start

Bootstrap a new project in the current directory:

```bash
uvx --from git+https://github.com/templ-project/cpp.git bootstrap .
```

Bootstrap a new project in a specific directory:

```bash
uvx --from git+https://github.com/templ-project/cpp.git bootstrap ./my-cpp-project
```

### Arguments

#### Target Directory

Specify a target directory as an argument (defaults to current directory):

```bash
uvx --from git+https://github.com/templ-project/cpp.git bootstrap ./my-cpp-project
```

#### Project Name (Optional)

Specify a custom project name with `--project-name`. If not provided, the project name will be extracted from the target directory name:

```bash
# Project name will be automatically extracted from directory name
uvx --from git+https://github.com/templ-project/cpp.git bootstrap ./awesome-game

# Custom project name
uvx --from git+https://github.com/templ-project/cpp.git bootstrap --project-name cool-lib ./my-project-dir
```

### Complete Examples

**Standard project in current directory:**

```bash
uvx --from git+https://github.com/templ-project/cpp.git bootstrap .
```

**New project in specific directory (project name auto-extracted):**

```bash
uvx --from git+https://github.com/templ-project/cpp.git bootstrap ./my-awesome-cpp-project
# Project name will be: "my-awesome-cpp-project"
```

**Custom project name:**

```bash
uvx --from git+https://github.com/templ-project/cpp.git bootstrap --project-name neural-network ./ai-project
# Project name will be: "neural-network"
```

## What the Bootstrap Script Does

The bootstrap script performs the following actions:

1. **Clones Template Repository**
   - Downloads the latest template from GitHub
   - Validates target directory is empty

2. **Removes Git History**
   - Deletes `.git` directory to start fresh

3. **Removes Bootstrap Artifacts**
   - Deletes `_install` directory (this directory!)
   - Removes the bootstrap script itself

4. **Updates Project Metadata**
   - Updates `CMakeLists.txt` project name to `my-cpp-project`
   - Updates `vcpkg.json` name and version
   - Updates `xmake.lua` project configuration
   - Updates `README.md` with placeholder content

## After Bootstrap

After running the bootstrap script, follow these steps:

1. **Update project configuration**

   ```bash
   # Edit the following files and update project details:
   # - CMakeLists.txt (project name, description)
   # - vcpkg.json (name, description)
   # - xmake.lua (project name)
   # - README.md (title, description, repository URL)
   ```

2. **Install dependencies**

   ```bash
   # Using Conan
   conan install . --build=missing

   # OR using vcpkg
   vcpkg install
   ```

3. **Build the project**

   ```bash
   # Using CMake
   cmake -B build -DCMAKE_CXX_COMPILER=clang++
   cmake --build build --parallel

   # OR using XMake
   xmake build
   ```

4. **Run tests**

   ```bash
   # With CMake
   cd build && ctest

   # With XMake
   xmake test
   ```

5. **Initialize git**

   ```bash
   git init
   git add .
   git commit -m "Initial commit from template"
   ```

6. **Start developing!**

   ```bash
   # Run the application
   ./build/src/my-cpp-project  # CMake
   xmake run my-cpp-project    # XMake
   ```

## Development

If you need to modify the bootstrap script:

1. Edit `_install/bootstrap.py`
2. Test locally by running:

   ```bash
   python _install/bootstrap.py [path]
   ```

3. Commit and push changes to the template repository

## Troubleshooting

### Script Not Found

If you get "script not found" errors, ensure:

1. You have Python 3.8 or higher installed
2. `uvx` is installed (`python -m pip install --user pipx && pipx ensurepath`)
3. You have internet connectivity to access GitHub

### Git Clone Failed

If the git clone fails, ensure:

1. Git is installed and available in PATH
2. You have internet connectivity
3. You have access to <https://github.com/templ-project/cpp>

### Target Directory Not Empty

The bootstrap script requires an empty target directory. If you get this error:

1. Choose a different directory name
2. Or remove existing files from the target directory

### Permission Errors

On Unix-like systems, ensure the bootstrap script is executable:

```bash
chmod +x _install/bootstrap.py
```
