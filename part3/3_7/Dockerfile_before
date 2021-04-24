FROM node:12-alpine
WORKDIR /app/expressdevops
COPY . ./
RUN npm install --only=prod

CMD ["npm", "start"]