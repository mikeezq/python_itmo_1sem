SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

docker build -t pdf-converter "${SCRIPT_DIR}"
docker run -it -v ${SCRIPT_DIR}/artifacts:/etc/hw_2/artifacts pdf-converter