/* Assemble telemetry into fixed-size buffer. No dynamic alloc. */
#include <stdint.h>
#include <stddef.h>

#define PKT_MAX_SIZE 256U
#define SUCCESS 0
#define ERR_OVERFLOW 1
#define ERR_BAD_ARG 2

typedef uint8_t status_t;

/* Safe helper: returns number of bytes written or error code via status. */
static size_t safe_append(uint8_t *buf, size_t buf_len,
                          size_t pos, const uint8_t *data,
                          size_t data_len, status_t *st)
{
    if ((buf == NULL) || (data == NULL) || (st == NULL)) { *st = ERR_BAD_ARG; return 0; }
    if (pos > buf_len) { *st = ERR_OVERFLOW; return 0; }
    if (data_len > (buf_len - pos)) { *st = ERR_OVERFLOW; return 0; }
    /* Copy loop with explicit bounds. */
    for (size_t i = 0U; i < data_len; ++i) { buf[pos + i] = data[i]; }
    *st = SUCCESS;
    return data_len;
}

/* Public API: assemble packet fields. Deterministic control flow. */
status_t assemble_telemetry(uint8_t *out_buf, size_t out_len,
                            uint16_t pkt_id, const uint8_t *payload,
                            size_t payload_len, size_t *pkt_size)
{
    status_t st = SUCCESS;
    size_t pos = 0U;
    if ((out_buf == NULL) || (pkt_size == NULL)) { return ERR_BAD_ARG; }
    if (out_len < PKT_MAX_SIZE) { return ERR_OVERFLOW; } /* enforce buffer size */

    /* Header (fixed 4 bytes) */
    uint8_t hdr[4U];
    hdr[0U] = (uint8_t)((pkt_id >> 8) & 0xFFU);
    hdr[1U] = (uint8_t)(pkt_id & 0xFFU);
    hdr[2U] = (uint8_t)((payload_len >> 8) & 0xFFU);
    hdr[3U] = (uint8_t)(payload_len & 0xFFU);

    if (safe_append(out_buf, out_len, pos, hdr, sizeof(hdr), &st) != sizeof(hdr)) { return st; }
    pos += sizeof(hdr);

    /* Payload (bounded) */
    if (payload_len > (PKT_MAX_SIZE - pos)) { return ERR_OVERFLOW; } /* final safety check */
    if (safe_append(out_buf, out_len, pos, payload, payload_len, &st) != payload_len) { return st; }
    pos += payload_len;

    /* Simple checksum (deterministic low-cost) */
    uint8_t csum = 0U;
    for (size_t i = 0U; i < pos; ++i) { csum = (uint8_t)(csum + out_buf[i]); }
    if (safe_append(out_buf, out_len, pos, &csum, 1U, &st) != 1U) { return st; }
    pos += 1U;

    *pkt_size = pos;
    return SUCCESS;
}