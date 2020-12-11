rm -rf layer/core/
mkdir -p layer/core/python
cp -r snail layer/core/python
cp -r models layer/core/python
cp -r snippets layer/core/python
[[ ! -d layer/python_libs ]] && sh scripts/layer-build.sh