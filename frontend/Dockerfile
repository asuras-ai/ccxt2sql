FROM node:14

WORKDIR /app

COPY package.json ./
#COPY package-lock.json . || true

RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "start"]
