DOCKERFILE_PATH="./scripts/build/Dockerfile"
CLOUD_BUILD_FILEPATH="./scripts/build/cloud_build.yaml"

#Build and push docker image to container resgitry
SUBSTITUTIONS_BUILD="_SERVICE_IMAGE=$SERVICE_IMAGE_URL,_SERVICE_IMAGE_VERSION=$SERVICE_IMAGE_VERSION,_DOCKERFILE_PATH=$DOCKERFILE_PATH"
gcloud builds submit --config=$CLOUD_BUILD_FILEPATH --project=$PROJECT_ID --substitutions="$SUBSTITUTIONS_BUILD"
