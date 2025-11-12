FROM node:20-alpine

WORKDIR /app

COPY package*.json ./
RUN npm ci --only=production

COPY tsconfig.json ./
COPY src ./src

RUN npm install --save-dev typescript && npm run build && npm prune --production

EXPOSE 9000

ENV PORT=9000

CMD ["node", "dist/index.js"]
